function reverseString(str) {
    return str.split('').reverse().join('');
}
reverseString('string'); // "gnirts"
console.log(reverseString('string'))

// _________________________________________

function reverseString2(str) {
    return [...String(str)].reverse().join('');
}
console.log(reverseString2('stackoverflow')); // "wolfrevokcats"
console.log(reverseString2(1337)); // "7331"
console.log(reverseString2([1, 2, 3])); // "3,2,1"

// _________________________________________

function reverse(string) {
    var strRev = "";
    for (var i = string.length - 1; i >= 0; i--) {
        strRev += string[i];
    }
    return strRev;
}
console.log(reverse("zebra")); // "arbez"

// __________________________________________

var arr = ["bananas", "cranberries", "apples"];
arr.sort(function (a, b) {
    return a.localeCompare(b);
});
console.log(arr); // [ "apples", "bananas", "cranberries" ]

// ___________________________________________

const AnimalSays = {
    dog() {
        return 'woof';
    },
    cat() {
        return 'meow';
    },
    lion() {
        return 'roar';
    },
    // ... other animals
    default() {
        return 'moo';
    }
};
// The above object can be used as follows:
function makeAnimalSpeak(animal) {
    // Match the animal by type
    const speak = AnimalSays[animal] || AnimalSays.default;
    console.log(animal + ' says ' + speak());
}
// Results:
makeAnimalSpeak('dog') // => 'dog says woof'
makeAnimalSpeak('cat') // => 'cat says meow'
makeAnimalSpeak('lion') // => 'lion says roar'
makeAnimalSpeak('snake') // => 'snake says moo'