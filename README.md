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

# Schemat bazy danych (stan na 10.05)

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

### Obliczanie liczby wolnych miejsc dla danego lotu

Przy obliczaniu liczby wolnych miejsc do bazy wysyłane jest następujące zapytanie
SELECT COUNT(\*) AS "\_\_count" FROM "Airplanes_reservation" WHERE ("Airplanes_reservation"."flight_id" = 3 AND "Airplanes_reservation"."paid")

Mając liczbę aktywnych rezerwacji odejmujemy ją w pythonie od liczby wolnych miejsc, dzięki czemu uzyskujemy finalną liczbę
