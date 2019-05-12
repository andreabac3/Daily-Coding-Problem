
fn main() {
    println!("{}",solve("11100010".to_string()));
    // assertResult = '11010001'
    println!("{}",solve("10101010".to_string()));
    // assertResult = '01010101'

}

fn solve(mut binary_vector:String ) -> String {
    let mut skip:bool = false;
    let mut i:usize = 0;
    let lenght:usize = binary_vector.len();
    while i < (lenght - 1) {
        if skip {
            skip = false;
            i = i + 1;
            continue;
        }
        if binary_vector.chars().nth(i).unwrap() == '1' && binary_vector.chars().nth(i+1).unwrap() == '0'{
            binary_vector.replace_range(i..i+2, "01");
            skip = true;
        }
        i = i + 1;
    }
    return binary_vector;
}

