function getNthFib(n) {
    // Write your code here.
   if(n <= 1){
       return 0;
   }
   let array = [0,1];
   while(array.length < n){
     array.push(array[array.length -1] + array[array.length -2])
   }
      return array[array.length -1]
  
  }
  
  // Do not edit the line below.
  exports.getNthFib = getNthFib;
  