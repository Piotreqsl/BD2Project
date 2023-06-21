# System rezerwacji lotów

## Adrian Stahl, Aleksandra Sobiesiak, Piotr Śliperski

# Opis

Aplikacja webowa do rezerwowania lotów i ich obsługi

# Tabele

- Loty - Flight
- Lotniska - Airport
- Pasażerowie - Profile
    - Powiązane z tabelą użytkowników - User, potrzebnej do autentykacji 
- Rezerwacje - Reservation
- Samoloty - Plane
- Pracownicy - Worker

# Technologie

- Postgresql
- Django + Python
- Front - HTML + CSS

# Role

- Menadżer - zarządza rezerwacjami, lotami
- Pasażer (klient) - może zarezerwować lot

# Funkcjonalności

- Pasażer
  - Rezerwacja biletu na przelot
  - Przeglądanie dostępnych lotów
  - Anulowanie rezerwacji
- Menadżer
  - Dodawanie / edytowanie / usuwanie lotów
  - Potwierdzenie / odrzucenie rezerwacji
  - Dodawanie / edytowanie / usuwanie wszelkich tabel

# Schemat bazy danych

![Schemat](/schema2.png)

# Jakie zapytania idą do bazy przy zapytaniach CRUD

## Na przykładzie tabeli airports

### Wypisanie wszystkich lotnisk

```sql
SELECT "Airplanes_airport"."id", "Airplanes_airport"."name", "Airplanes_airport"."country", "Airplanes_airport"."town" 
FROM "Airplanes_airport"
```

### Szczegółowe informacje o wybranym lotnisku
```sql
SELECT "Airplanes_airport"."id", "Airplanes_airport"."name", "Airplanes_airport"."country", "Airplanes_airport"."town" 
FROM "Airplanes_airport" 
WHERE "Airplanes_airport"."id" = 2 
LIMIT 21
```
### Edycja lotniska

```sql
UPDATE "Airplanes_airport" 
SET "name" = 'Port lotniczy gdańsk', "country" = 'Poland', "town" = 'Gdańsk' 
WHERE "Airplanes_airport"."id" = 3; args=('Port lotniczy gdańsk', 'Poland', 'Gdańsk', 3)
```
### Usuwanie lotniska
```sql
(0.047) DELETE FROM "Airplanes_worker" 
WHERE "Airplanes_worker"."working_on_id" 
IN (3); args=(3,)
```
```sql
(0.046) DELETE FROM "Airplanes_airport" 
WHERE "Airplanes_airport"."id" 
IN (3); args=(3,)
```

Jak widzimy usuwanie dzieje się kaskadowo (co prawda tabela workers pozostaje nieużywana w naszym systemie, jednak wpierw usuwani są pracownicy pracujący na danym lotnisku)

## Działania związane z rezerwacjami
### Tworzenie nowej rezerwacji

```sql
INSERT INTO "Airplanes_reservation" ("person_id", "flight_id", "status", "date") 
VALUES (3, 2, 'PENDING', '2023-06-21T05:17:07.178962+00:00'::timestamptz) RETURNING "Airplanes_reservation"."id"; args=(3, 2, <Status.PENDING: 'PENDING'>, datetime.datetime(2023, 6, 21, 5, 17, 7, 178962, tzinfo=<UTC>))
```

### Obliczanie liczby wolnych miejsc dla danego lotu

Przy obliczaniu liczby wolnych miejsc do bazy wysyłane jest następujące zapytanie
```sql
SELECT COUNT(\*) AS "\_\_count" 
FROM "Airplanes_reservation" 
WHERE (("Airplanes_reservation"."flight_id" = 2 
  AND "Airplanes_reservation"."status" = 'ACCEPTED') 
  OR ("Airplanes_reservation"."flight_id" = 2 
  AND "Airplanes_reservation"."status" = 'PENDING')); args=(2, <Status.ACCEPTED: 'ACCEPTED'>, 2, <Status.PENDING: 'PENDING'>)
```

Odpowiednie metody w klasie Flight powiązanej z modelem lotów
```python
def count_reservations(self):
    return Reservation.objects.filter(
        Q(flight=self.id, status=Status.ACCEPTED) | Q(flight=self.id, status=Status.PENDING)
    ).count()

def free_places(self):
    return self.no_seats - self.count_reservations()
```

Mając liczbę aktywnych rezerwacji odejmujemy ją w metodzie free_places od liczby wolnych miejsc, dzięki czemu uzyskujemy finalną liczbę

## Działania związane z użytkownikami
### W jaki sposób tworzony jest nowy użytkownik?
```sql
INSERT INTO "auth_user" ("password", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined") 
VALUES ('pbkdf2_sha256$260000$18uX3UwJt3igUDugFQIXid$8Ue+wb184ic7OooMXWpk9HS/vWiwgAHgBc9iOyUpE8o=', NULL, false, 'Piotreqsl', 'Piotr', 'Śliperski', 'piotreksl2002@go2.pl', false, true, '2023-06-21T05:09:38.070722+00:00'::timestamptz) RETURNING "auth_user"."id"; args=('pbkdf2_sha256$260000$18uX3UwJt3igUDugFQIXid$8Ue+wb184ic7OooMXWpk9HS/vWiwgAHgBc9iOyUpE8o=', None, False, 'Piotreqsl', 'Piotr', 'Śliperski', 'piotreksl2002@go2.pl', False, True, datetime.datetime(2023, 6, 21, 5, 9, 38, 70722, tzinfo=<UTC>))
```
Powyższe polecenie wygenerowane zostało przez django auth, podczas rejestracji nowego użytkownika

Odpowiadające funkcja generująca widok i formularz rejestracji w kodzie pythonowym
```python
def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            # obsługa rejestracji
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('airplanes:home')

            # nie udało się
            info = "The registration was unsuccessful"
            return render(request, 'register.html', {"form": form, "info": info})
        else:
            info = "The password is not strong enough"
            return render(request, 'register.html', {"form": form, "info": info})
    else:
        form = RegisterUserForm()
        return render(request, 'register.html', {"form": form})
```
```python
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
```

### Pobieranie rezerwacji użytkownika
Wysyłane zapytanie
```sql
SELECT "Airplanes_reservation"."id", "Airplanes_reservation"."person_id", "Airplanes_reservation"."flight_id", "Airplanes_reservation"."status", "Airplanes_reservation"."date" 
FROM "Airplanes_reservation" 
WHERE ("Airplanes_reservation"."date" <= '2023-06-21T05:14:21.100492+00:00'::timestamptz 
  AND "Airplanes_reservation"."person_id" = 3); args=(datetime.datetime(2023, 6, 21, 5, 14, 21, 100492, tzinfo=<UTC>), 3)
```
Odpowiadający widok w kodzie pythonowym
```python
def manage_reservations(request):
    reservations = Reservation.objects.filter(person=request.user.profile, date__lte=timezone.now())
    return render(request, 'my_reservations.html', {"reservations": reservations})
```
