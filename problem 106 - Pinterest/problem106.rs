
fn main(){
    let mut array:[i32; 4] = [2, 0, 1, 0];
    println!("{}", solve(&array));
    array = [1, 1, 0, 1];
    println!("{}", solve(&array));
}

fn solve(array: &[i32; 4]) -> bool {
    let lenght:usize = array.len() - 1;
    if array[0] == 0 {return false;}
    let mut i:usize = (1 + array[0] - 1) as usize;
    while i < lenght {
        if array[i] == 0 {return false;}
        i = (array[i] + i as i32) as usize;
    }
    return true;
}
