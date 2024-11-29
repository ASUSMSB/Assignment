import requests

url="https://physics.lk/gurumandala_students/register_new_student.php"

data= {
    "first_name": "asus",
    "last_name": "msb",
    "date_of_birth_year": "2006",
    "date_of_birth_month": "6",
    "date_of_birth_day": "6",
    "password": "Asus@2000",
	"password_confirm": "Asus@2000",
    "mobile": "0764087299"
}
response=requests.post(url,data)
print(response)
