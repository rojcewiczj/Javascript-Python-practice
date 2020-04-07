alpha_values = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4,
    "e" : 5,
    "f" : 6,
    "g" : 7,
    "h" : 8,
    "i" : 9,
    "j" : 10,
    "k" : 11,
    "l" : 12,
    "m" : 13,
    "n" : 14,
    "o" : 15,
    "p" : 16,
    "q" : 17,
    "r" : 18,
    "s" : 19,
    "t" : 20,
    "u" : 21,
    "v" : 22,
    "w" : 23,
    "x" : 24,
    "y" : 25,
    "z" : 26
}
function balanced(word) {
whole = word.length
half = whole / 2
later_half = whole / 2
if (word.length % 2 == 1){
        half = Math.round((whole / 2) - 1)
}

first_half = word.slice(0, half)

if (word.length % 2 == 1){
    later_half = Math.round((whole / 2) - 1) + 1
}

second_half = word.slice(later_half, whole)

first_half_values = []
second_half_values = []

for(index in first_half) {
    first_half_values.push(alpha_values[first_half[index]])
}
for(index in second_half) {
    second_half_values.push(alpha_values[second_half[index]])
}

first_half_total = first_half_values.reduce((a, b) => a + b, 0)
second_half_total = second_half_values.reduce((a, b) => a + b, 0)

if(first_half_total == second_half_total) {
return true
}
else {
return false
}

}
// checks if the first half of the word is equivalent to the second half, based on a value scale