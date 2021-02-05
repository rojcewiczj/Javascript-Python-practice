function minimumWaitingTime(queries) {
    // Write your code here.
      queries.sort((a,b) => a - b);
      console.log(queries)
      let total = 0
      let totals = []
      let i = 1;
      while(i < queries.length){
          total += queries[i-1];
          totals.push(total);
          console.log(total)
          i ++
      }
      let final_total = 0;
      for(var num of totals){
      final_total += num
      }
      console.log(final_total)
    return final_total;
  }
  
  // Do not edit the line below.
  exports.minimumWaitingTime = minimumWaitingTime;