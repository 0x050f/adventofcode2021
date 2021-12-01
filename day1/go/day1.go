package main

import (
	"bufio"
	"log"
	"fmt"
	"os"
	"strconv"
)

func part1() {
	fmt.Println("--- Part One ---");
	file, err := os.Open("../input")
	if err != nil {
		log.Fatal(err)
		os.Exit(1)
	}
	defer file.Close()
	count := 0
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
		os.Exit(1)
	}
	prev_value, err := strconv.Atoi(scanner.Text())
	scanner.Scan()
	value, err := strconv.Atoi(scanner.Text())
	for scanner.Scan() {
		if prev_value < value {
			count++
		}
		prev_value = value
		value, err = strconv.Atoi(scanner.Text())
	}
	if prev_value < value {
		count++
	}
	fmt.Printf("Result: %d 'increased'\n", count);
}

func sum_array(array []int) int {
	sum := 0

	for i := range array {
		sum += array[i]
	}
	return sum
}

func part2() {
	fmt.Println("--- Part One ---");
	file, err := os.Open("../input")
	if err != nil {
		log.Fatal(err)
		os.Exit(1)
	}
	defer file.Close()
	count := 0
	scanner := bufio.NewScanner(file)
	var window1[3]int
	var window2[3]int
	for i := range window1 {
		scanner.Scan()
		if err := scanner.Err(); err != nil {
			log.Fatal(err)
			os.Exit(1)
		}
		window1[i], err = strconv.Atoi(scanner.Text())
	}
	for i := range window2[:len(window2) - 1]{
		window2[i] = window1[i + 1]
	}
	scanner.Scan()
	window2[2], err = strconv.Atoi(scanner.Text())
	for scanner.Scan() {
		if sum_array(window1[:]) < sum_array(window2[:]) {
			count++
		}
		for i := range window1 {
			window1[i] = window2[i]
		}
		for i := range window2[:len(window2) - 1]{
			window2[i] = window2[i + 1]
		}
		window2[len(window2) - 1], err = strconv.Atoi(scanner.Text())
	}
	if sum_array(window1[:]) < sum_array(window2[:]) {
		count++
	}
	fmt.Printf("Result: %d 'increased'\n", count);

}

func main() {
	part1();
	part2();
}
