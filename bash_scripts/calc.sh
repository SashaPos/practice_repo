#!/bin/bash
#Nothing special. Just trying to write functions
input_func() {
	read -p "Enter the first number: " first_num
	read -p "Enter the second number: " second_num
	read -p "Enter the desired operation (a, s, m, d): " operation
}

add() {
	echo $(($first_num + $second_num))
}

substract() {
	echo $(($first_num - $second_num))
}

multiply() {
	echo $(($first_num * $second_num))
}

divide() {
	echo $(($first_num / $second_num))
}

calculation() {
	if [[ $operation == "a" ]]; then
		add
	elif [[ $operation == "s" ]]; then
		substract
	elif [[ $operation == "m" ]]; then
		multiply
	elif [[ $operation == "d" ]]; then
		divide
	else
		echo "Wrong operation: " $operation ; 
		echo "TRY AGAIN" ; input_func ; calculation
	fi
}

input_func
calculation
