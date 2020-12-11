
function sort(array) {
	for (var i=1; i<array.length;i++) {
		for (var j=0; j<i;j++) {
			if (array[i] < array[j]) {
				temp = array[i];
				array[i] = array[j];
				array[j] = temp;
			}
		}
	}
	return array;
}


input = [1,10,5,15,2,7,28,900,45,18,27];

result = sort(input);

console.log(result);
