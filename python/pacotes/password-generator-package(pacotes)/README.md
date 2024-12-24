# package_name

Description. 
The package package_name is used to:
	- Gerador de senhas.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install password_generator

```bash
pip install password_generator_guirib00
```

## Usage

```python
from password_generator_guirib00 import generator

password = generator.generate_simple_password(10)
print(password)

password_complex = generator.generate_complex_password(16)
print(password_complex)
```

## Author
guirib00

## License
[MIT](https://choosealicense.com/licenses/mit/)