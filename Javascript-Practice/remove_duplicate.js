function removeDuplicatesFromLinkedList(linkedList) {
    let current = linkedList;
      while(current.next != null){
         if(current.next.value === current.value){
            if(current.next.next != null){
                current.next = current.next.next
                       }
                   else{
                        current.next = null;
                   }
               }
             else{
              current = current.next;
                }
      }
    return linkedList;
  }
  
  // Do not edit the lines below.
  exports.LinkedList = LinkedList;
  exports.removeDuplicatesFromLinkedList = removeDuplicatesFromLinkedList;
  