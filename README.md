# Ruchy Browna

## Temat projektu

Zagadnieniem naszego projektu było zaimplentowanie realistycznej symulacji ruchów Browna. Założyliśmy, że modelujemy ruch cząsteczki pyłku w płynie. W naszym przypadku cząsteczka pyłu ok. 30 razy cięższa i ok. 3,5 raza większa od cząsteczki płynu, których było 150.

## Wykorzystane oprogramowanie

Projekt został zaimplementowany w bibliotece do tworzenia gier i aplikacji multimedialnych `pygame`. Wykorzystaliśmy tą paczkę, ponieważ potrzebowaliśmy środowiska do tworzenia symulacji w czasie rzeczywistym, a `pygame` jako relatywnie proste do użycia narzędzie nam to umożliwiło. Użyliśmy też `numpy` do matematyczny obliczeń oraz `jupyter` do stworzenia raportu i analizy poszczególnych wariantów ruchów.

## Uruchomienie

Po ściągnięciu repozytorium na lokalny sprzęt należy zainicjować nowe wirtualne środowisko:

```shell
python -m venv .venv
```

Następnie zależnie od platformy trzeba doinstalować wszystkie zależności i można uruchomić projekt:

### Linux

```shell
.venv/bin/pip install -r requirements.txt
.venv/bin/python main.py
```

### Windows

```shell
.venv/Scripts/pip install -r requirements.txt
.venv/Scripts/python main.py
```

