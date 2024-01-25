# Projekt procesu CICD

Zespół:
- Maciej Marcinkiewicz
- Krysztof Piotrowski
- Łukasz Pokorzyński

# Aplikacja

W procesie CICD wykorzystana została aplikacja napisana w języku Python wraz z frameworkiem Flask, którą mieliśmy okazję poznawać w ramach laboratorium na przedmiocie TBO.

# Opis zaimplementowanego procesu CICD

W ramach procesu CICD stworzone zostały 3 pliki o rozszerzeniu .yml:
- ci_lastest
- cd_latest
- ci_cd_beta

Dwie pierwsze konfiguracje dotyczą procesu CICD przeprowadzanego dla gałęzi master. Trzecia konfiguracja dotyczy procesu, który zachodzi na nowych gałęziach utworzonych przez użytkowników repozytorium.

## ci_latest
Plik konfiguracyjny może zostać uruchomiony przez operację utworzenia pull requesta w typach opened, reopened lub edited lub w sposób manualny dzięki tagowi *workflow_dispatch*.  
W ramach tego procesu stworzone zostały następujące joby:

### test-unit
Uruchamia testy jednostkowe. Kolejne kroki i ich nazwy:  
- Checkout
- Set up Python; wykorzystywana jest ostatnia wersja Python3
- Install dependencies; instaluje potrzebne wymagania zdefiniowane w pliku requirements.txt
- Test with PyTest; testy do tego kroku umieszczone zostały w folderze tests

### test-sast
Uruchamia testy SAST. Wykorzystywane jest oprogramowanie gitleaks oraz bandit.  
Kolejne kroki i ich nazwy:
- Checkout
- Run gitleaks
- Install bandit package
- Run bandit
- Upload bandit results; wyniki są zapisywane do artefaktu bandit-results.html

### test-dast
Uruchamia testy DAST. Wykorzystywane jest oprogramowanie ZAProxy. Proces ten ma udzieloną permisję *write-all*.  
Kolejne kroki i ich nazwy:
- Checkout
- Deploy with use of SSH; tworzy obraz Dockerowy z aktualnej gałęzi
- ZAP Scan

### test-sca
Uruchamia testy SCA. Wykorzystuje oprogramowanie Dependency-Check.  
Kolejne kroki i ich nazwy:
- Checkout
- Run dependency check
- Upload dependency check; zawsze zapisuje wyniki testu do folderu reports w Workspace

## cd-latest
Plik konfiguracyjny może zostać uruchomiony przez operację push do gałęzi master.  
W ramach tego procesu stworzone zostały jeden job o nazwie build.

### build
Buduje aplikację znajdującą się na gałęzi master.  
Kolejne kroki i ich nazwy:
- Checkout
- Login to Docker Hub
- Set up Docker Buildx
- Build and push; zbudowana aplikacja jest przekazywana z tagiem *latest*.

## ci_cd_beta
Plik konfiguracyjny może zostać uruchomiony przez operację push do każdej gałęzi oprócz master lub w sposób manualny dzięki tagowi *workflow_dispatch*.  
W ramach tego procesu stworzone zostały joby pokrywajace się w nazwach oraz podejmowanych krokach jak w procesach ci_latest oraz cd_latest opisanych wyżej.  
Zamiast tagu *latest* używany jest tag *beta* dla budowanych aplikacji. Poprawne zbudowanie aplikacji wymaga pomyślnego przejścia wszystkich jobów z testami jednostkowymi, SAST, DAST i SCA, co zostało ujęte w jobie **build** w polu *needs*.
