# Linguist
це застосунок для полегшення процесу вивчення іноземної мови.


Створити модельки: 
Користувач (`User`)
- `id`
- `name`
- `email`
- `password`

Колода (`Deck`)
- `id`
- `name`
- `user_id`

Картка (`Card`) 
- `id` 
- `user_id` 
- `word` [слово англійською мовою]
- `translation` [його переклад українською]
- `tip` [та підказку до слова]


До кожної модельки створити функції для забезпечення базового функціоналу `CRUD`

- `user_create(name, email, password)`
- `user_get_by_id(user_id)`
- `user_update_name(user_id, name)`
- `user_change_passworf(user_id, old_password, new_password)`
- `user_delete_by_id(user_id)`


- `deck_create(name, user_id)`
- `deck_get_by_id(deck_id)`
- `deck_update(deck_id, name)`
- `deck_delete_by_id(deck_id)`


- `card_create(user_id, word, translation, tip)`
- `card_get_by_id(card_id)`
- `card_update(card_id, word=None, translation=None, tip=None)`
- `card_delete_by_id(card_id)`
