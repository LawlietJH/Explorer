# Explorer
## Version: v1.2.1

### Modo de Uso:
---
__Esta función devuelve un String con la ruta completa, nombre y extensión del archivo que se desea abrir.__
```python
from explorer import Explorer as ex
file_name = ex.getFileName()
print(file_name)
```
__Resultado:__
```ms
C:/Users/LawlietJH/Documents/GitHub/xD.txt
```
---
__Esta función devuelve un String con la ruta completa de la carpeta seleccionada.__
```python
from explorer import Explorer as ex
folder_path = ex.getFolderName()
print(folder_path)
```
__Resultado:__
```ms
C:/Users/LawlietJH/Documents/GitHub
```
---
__Esta función devuelve un String con la ruta completa, nombre y extensión del archivo que se desea crear y guardar.__
```python
from explorer import Explorer as ex
file_name_save = ex.getSaveFileName()
print(file_name_save)
```
__Resultado:__
```ms
C:/Users/LawlietJH/Documents/GitHub/xD.txt
```
---
