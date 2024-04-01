.venv\Scripts\activate

get-content envs\test.env | foreach {
    $name, $value = $_.split('=')
    set-content env:\$name $value
}

python app\manage.py test app
