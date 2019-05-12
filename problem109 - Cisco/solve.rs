
fn main() {
    println!("{}",solve("11100010".to_string()) == "11010001");
    // assertResult = '11010001'
    println!("{}",solve("10101010".to_string()) == "01010101");
    // assertResult = '01010101'
}

fn solve(mut input_string:String ) -> String {
    let mut i:usize = 0;
    let lenght:usize = input_string.len();
    while i < (lenght - 1) {
        if input_string.chars().nth(i).unwrap() == '1' && input_string.chars().nth(i+1).unwrap() == '0'{
            input_string.replace_range(i..i+2, "01");
        }
        else if input_string.chars().nth(i).unwrap() == '0' && input_string.chars().nth(i+1).unwrap() == '1'{
            input_string.replace_range(i..i+2, "10");
        }
        i = i + 2;
    }
    return input_string;
}
