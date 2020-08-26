## happy path
* start
  - utter_ask_name
* name_response
  - utter_greet
  - utter_ask_color
> check_asked_color


## blue path
> check_asked_color
* select_color{"client_color": "niebieski"}
  - slot{"client_color": "niebieski"}
  - action_color
  - utter_ask_age
> check_asked_age

## red path
> check_asked_color
* select_color{"client_color": "czerwony"}
  - slot{"client_color": "czerwony"}
  - action_color
  - utter_ask_age
> check_asked_agesta


## age path yes
> check_asked_age
* confirm
  - utter_age_ok
  - utter_goodby

## age path no
> check_asked_age
* denny
  - utter_age_no
  - utter_goodby