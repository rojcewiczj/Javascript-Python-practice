/// N is an array of Nodes, P is an array of Parent Nodes, n is a single node
/// the function tells you if n is the root, a leaf, or an inner node
function nodeType(N, P, n) {
	console.log("nodes: ", N)
	console.log("parents: ", P)
	len = N.length
	inc = 0
	parents = {}
    children = {}
	for (index in P) {
		parents[P[index]] = []
	}
	for (index in N) {
		children[N[index]] = []
	}
	while (len > 0){
		parents[P[inc]].push(N[inc])
	  inc +=1
		len -= 1
	}
	inc = 0
	len = N.length

	while (len > 0){
		children[N[inc]].push(P[inc])
	  inc +=1
		len -= 1
	}

    if (parents[n] == undefined && children[n]){
	    return "Leaf"
    }
    if  (children[n] == undefined && parents[n] || children[n] == -1){
	    return "Root"
    }
    if (children[n] && parents[n]){
		return "Inner"
	}
    else {
	    return "Not exist"
    }

}