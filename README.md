# System rezerwacji lotów

## Adrian Stahl, Aleksandra Sobiesiak, Piotr Śliperski

# Opis

Aplikacja webowa do rezerwowania lotów i ich obsługi

# Tabele

- Loty
- Lotniska
- Pasażerowie
- Rezerwacje
- Samoloty
- Pracownicy
- (opcjonalnie) Bagaże

# Technologie

- Postgresql
- Django + Python
- Front - HTML CSS

# Role

- Pracownik - zarządca rezerwacji
- Pracownik - zarządca lotami
- Admin
- Pasażer (klient)

# Funkcjonalności

- Pasażer
  - Rezerwacja biletu na przelot
  - Przeglądanie dostępnych lotów
  - Anulowanie rezerwacji
- Pracownik - zarządca rezerwacji
  - Potwierdzenie / odrzucenie rezerwacji
- Pracownik - zarządca lotami
  - Dodawanie / edytowanie / usuwanie lotów
- Administrator
  - Wszystkie funkcjonalności powyżej
  - Dodawanie / edytowanie / usuwanie wszelkich tabel

# Schemat bazy danych

![Schemat](/schema.png)

# Jakie zapytania idą do bazy przy zapytaniach CRUD

## Na przykładzie tabeli airports

### Wypisanie wszystkich lotnisk

SELECT "Airplanes_airport"."id", "Airplanes_airport"."name", "Airplanes_airport"."country", "Airplanes_airport"."town" FROM "Airplanes_airport"

### Szczegóły lotniska

SELECT "Airplanes_airport"."id", "Airplanes_airport"."name", "Airplanes_airport"."country", "Airplanes_airport"."town" FROM "Airplanes_airport" WHERE "Airplanes_airport"."id" = 2 LIMIT 21

### Edycja lotniska

UPDATE "Airplanes_airport" SET "name" = 'Port lotniczy gdańsk', "country" = 'Poland', "town" = 'Gdańsk' WHERE "Airplanes_airport"."id" = 3; args=('Port lotniczy gdańsk', 'Poland', 'Gdańsk', 3)

### Usuwanie lotniska

(0.047) DELETE FROM "Airplanes_worker" WHERE "Airplanes_worker"."working_on_id" IN (3); args=(3,)
(0.046) DELETE FROM "Airplanes_airport" WHERE "Airplanes_airport"."id" IN (3); args=(3,)

Jak widzimy usuwanie dzieje się kaskadowo (co prawda tabela workers pozostaje nieużywana w naszym systemie, jednak wpierw usuwani są pracownicy pracujący na danym lotnisku)

### Tworzenie nowej rezerwacji

INSERT INTO "Airplanes_reservation" ("person_id", "flight_id", "status", "date") VALUES (3, 2, 'PENDING', '2023-06-21T05:17:07.178962+00:00'::timestamptz) RETURNING "Airplanes_reservation"."id"; args=(3, 2, <Status.PENDING: 'PENDING'>, datetime.datetime(2023, 6, 21, 5, 17, 7, 178962, tzinfo=<UTC>))

### Obliczanie liczby wolnych miejsc dla danego lotu

Przy obliczaniu liczby wolnych miejsc do bazy wysyłane jest następujące zapytanie

SELECT COUNT(\*) AS "\_\_count" FROM "Airplanes_reservation" WHERE (("Airplanes_reservation"."flight_id" = 2 AND "Airplanes_reservation"."status" = 'ACCEPTED') OR ("Airplanes_reservation"."flight_id" = 2 AND "Airplanes_reservation"."status" = 'PENDING')); args=(2, <Status.ACCEPTED: 'ACCEPTED'>, 2, <Status.PENDING: 'PENDING'>)

Mając liczbę aktywnych rezerwacji odejmujemy ją w pythonie od liczby wolnych miejsc, dzięki czemu uzyskujemy finalną liczbę

### W jaki sposób tworzony jest nowy użytkownik?

INSERT INTO "auth_user" ("password", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined") VALUES ('pbkdf2_sha256$260000$18uX3UwJt3igUDugFQIXid$8Ue+wb184ic7OooMXWpk9HS/vWiwgAHgBc9iOyUpE8o=', NULL, false, 'Piotreqsl', 'Piotr', 'Śliperski', 'piotreksl2002@go2.pl', false, true, '2023-06-21T05:09:38.070722+00:00'::timestamptz) RETURNING "auth_user"."id"; args=('pbkdf2_sha256$260000$18uX3UwJt3igUDugFQIXid$8Ue+wb184ic7OooMXWpk9HS/vWiwgAHgBc9iOyUpE8o=', None, False, 'Piotreqsl', 'Piotr', 'Śliperski', 'piotreksl2002@go2.pl', False, True, datetime.datetime(2023, 6, 21, 5, 9, 38, 70722, tzinfo=<UTC>))

Powyższe polecenie wygenerowane zostało przez django auth, podczas rejestracji nowego użytkownika

### Pobieranie rezerwacji użytkownika

SELECT "Airplanes_reservation"."id", "Airplanes_reservation"."person_id", "Airplanes_reservation"."flight_id", "Airplanes_reservation"."status", "Airplanes_reservation"."date" FROM "Airplanes_reservation" WHERE ("Airplanes_reservation"."date" <= '2023-06-21T05:14:21.100492+00:00'::timestamptz AND "Airplanes_reservation"."person_id" = 3); args=(datetime.datetime(2023, 6, 21, 5, 14, 21, 100492, tzinfo=<UTC>), 3)
