function add(x, y) {
    return parseFloat(x) + parseFloat(y)
}

function add_arr_numbers(number_arr) {
    let sum = 0
    for (let i = 0; i < number_arr.length; i++) {
        sum = add(number_arr[i], sum)
    }
    return sum;
}

function sumVat(x, y) {
    return parseFloat(x) + y;
}

function add_vat_numbers(number_arr) {
    let sum = 0
    for (let i = 0; i < number_arr.length; i++) {
        sum = sumVat(number_arr[i], sum)
    }
    return sum;
}

function find_rect_area(length, breadth) {
    return length * breadth;
}

function find_min_area(rec_values_arr) {
    let w = parseInt(rec_values_arr[0])
    let h = parseInt(rec_values_arr[1])
    let W = parseInt(rec_values_arr[2])
    let H = parseInt(rec_values_arr[3])
    let rec1_area = find_rect_area(w, h);
    let rec2_area = find_rect_area(W, H);
    let rec_min_area = find_rect_area(Math.min(w, W), Math.min(h, H))
    let total_area = rec1_area + rec2_area - rec_min_area
    return total_area;
}

function find_next_date(given_date_arr) {
    let year = parseInt(given_date_arr[0])
    let month = parseInt(given_date_arr[1])
    let day = parseInt(given_date_arr[2])
    const current_date = new Date(year, month - 1, day)
    const one_day = 24 * 60 * 60 * 1000
    const next_date = new Date(current_date.getTime() + one_day)
    return (next_date.getFullYear() + "-" + (next_date.getMonth() + 1) + "-" + next_date.getDate());
}

function prepare_point_objects(str_elements_arr) {
    const point_A = {
        x: parseFloat(str_elements_arr[0]),
        y: parseFloat(str_elements_arr[1]),
    }
    const point_B = {
        x: parseFloat(str_elements_arr[2]),
        y: parseFloat(str_elements_arr[3]),
    }
    return [point_A, point_B]
}

function find_distance(point_A, point_B) {
    let x_diff = point_A.x - point_B.x
    let y_diff = point_A.y - point_B.y
    let distance = Math.sqrt(x_diff * x_diff + y_diff * y_diff)
    return (distance)
}

function findOccurence(word, letter) {
    let letter_occur = 0
    const char_array = word.split('')

    for (let i = 0; i < char_array.length; i++) {
        if (char_array[i] == letter) {
            letter_occur++
        }
    }
    return letter_occur;
}

function display_numbers(number_upto_arr) {
    let number_upto = parseInt(number_upto_arr[0])
    let print_numbers = ''
    for (let i = 1; i <= number_upto; i++) {
        //concatination 
        print_numbers = print_numbers + i

    }
    return (print_numbers)
}


function prepare_person_objects(person_details) {
    const person1 = {
        name: person_details[1],
        age: parseInt(person_details[2]),
    }
    person2 = new Object()
    person2.name = person_details[3]
    person2.age = parseInt(person_details[4])

    return [person1, person2]
}

function filterByMinAge(minAge, person_arr) {
    for (let i = 0; i < person_arr.length; i++) {
        let person = person_arr[i]
        if (minAge < person.age) {
            return (person)
        }
    }
}