#!/usr/bin/env bash
echo "what operation do you like?"
echo "1. Convert to base64
2. Convert to normal text"
read n
case $n in
	1)
		echo "enter encoded text"; read encoded_text; echo "$encoded_text" | base64 -d
		;;
	2)
		echo "enter text"; read text; echo $text | base64
		;;
	*)
		echo "invalid option"
		;;
esac

