
let city_field = document.getElementById('id_city')
let team_field = document.getElementById('id_team')
team_field.innerHTML = '<option value="">Выберите бригаду</option>'
let people_field = document.getElementById('id_amount_people')
let head_field = document.getElementById('id_head')
let qual_field = document.getElementById('id_qualification')


city_field.addEventListener('change', getCity)
async function getCity(e) {
    people_field.value = ""
    head_field.value = ""
    qual_field.value = ""
    city_id = e.target.value;

    const response = await fetch(
        `/api/teams/${city_id}`
    )
    teams_array = await response.json()
    team_field.innerHTML = '<option value="">Выберите бригаду</option>'
    for (let index = 0; index < teams_array.length; index++) {
        const element = teams_array[index];
        team_field.innerHTML += `<option value=${element['id']}>${element['name']}</option>`
    }
}

team_field.addEventListener('change', getTeam)
async function getTeam(e) {
    team_id = e.target.value;

    const response = await fetch(`/api/object/${team_id}`)
    let data_object = await response.json()
    const data = JSON.parse(data_object)
    console.log(data)
    people_field.value = data['amount_people']
    head_field.value = data['head']
    qual_field.value = data['qualification']
}
