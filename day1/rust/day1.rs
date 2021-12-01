use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn part1() -> io::Result<()> {
	println!("--- Part One ---");
	let file = File::open("../input")?;
	let reader = BufReader::new(file);

	let mut iterator = reader.lines();
	let mut value: i32 = iterator.next().unwrap().unwrap().parse().unwrap();
	let mut prev_value: i32 = value;
	let mut count: i32 = 0;
	for line in iterator {
		if value != prev_value {
//			print!("{} -> {} ", prev_value, value);
			if value > prev_value {
//				println!("(increased)");
				count += 1;
			}
/*			else if value < prev_value {
				println!("(decreased)");
			}
			else {
				println!("(no change)");
			}*/
		}
		prev_value = value;
		value = line.unwrap().parse().unwrap();
	}
//	print!("{} -> {} ", prev_value, value);
	if value > prev_value {
		count += 1;
	}
	println!("Result: {} 'increased'", count);

	Ok(())
}

fn sum_array(array: &[i32]) -> i32 {
	let mut sum = 0;
	let mut i = 0;

	while i < array.len() {
		sum += array[i];
		i += 1;
	}
	return sum;
}

fn part2() -> io::Result<()> {
	println!("--- Part Two ---");
	let file = File::open("../input")?;
	let reader = BufReader::new(file);

	let mut window1: [i32; 3] = [0, 0, 0];
	let mut window2: [i32; 3] = [0, 0, 0];
	let mut iterator = reader.lines();
	window1[0] = iterator.next().unwrap().unwrap().parse().unwrap();
	window1[1] = iterator.next().unwrap().unwrap().parse().unwrap();
	window1[2] = iterator.next().unwrap().unwrap().parse().unwrap();
	window2[0] = window1[1];
	window2[1] = window1[2];
	window2[2] = iterator.next().unwrap().unwrap().parse().unwrap();
	let mut count: i32 = 0;
	for line in iterator {
//		print!("{:?} - {:?} ", window1, window2);
		if sum_array(&window1) < sum_array(&window2) {
//			println!("(increased)");
			count += 1;
		}
/*		else if sum_array(&window1) > sum_array(&window2) {
			println!("(decreased)");
		}
		else {
			println!("(no change)");
		}*/
		window1[0] = window1[1];
		window1[1] = window1[2];
		window1[2] = window2[2];
		window2[0] = window2[1];
		window2[1] = window2[2];
		window2[2] = line.unwrap().parse().unwrap();
	}
//	print!("{:?} - {:?} ", window1, window2);
	if sum_array(&window1) < sum_array(&window2)  {
		count += 1;
	}
	println!("Result: {} 'increased'", count);

	Ok (())
}

fn main() {
	part1().map_err(|err| println!("{:?}", err)).ok();
	part2().map_err(|err| println!("{:?}", err)).ok();
}
