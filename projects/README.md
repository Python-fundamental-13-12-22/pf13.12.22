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
- `tip` [підказку до слова]


До кожної модельки створити функції для забезпечення базового функціоналу `CRUD`

User
- `user_create(name, email, password) -> User`
- `user_get_by_id(user_id) -> User`
- `user_update_name(user_id, name) -> User`
- `user_change_passworf(user_id, old_password, new_password) -> bool`
- `user_delete_by_id(user_id) -> bool`

Deck
- `deck_create(name, user_id) -> Deck`
- `deck_get_by_id(deck_id) -> Deck`
- `deck_update(deck_id, name) -> Deck`
- `deck_delete_by_id(deck_id) -> bool`

Card
- `card_create(user_id, word, translation, tip) -> Card`
- `card_get_by_id(card_id) -> Card` 
- `card_filter(sub_word) -> tuple[Card]` повертає список тих слів у яких `sub_word` зустрічається у `word` або `translation` або `tip`
- `card_update(card_id, word=None, translation=None, tip=None) -> Card`
- `card_delete_by_id(card_id) -> bool`
