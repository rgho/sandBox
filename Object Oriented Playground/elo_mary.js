
// THIS IS BASICALALLY WHAT HAPPENS WHEN YOU MAKE A CONSTRUCTOR
// HOWEVER THE BELOW WAY IS THE NORMAL WAY
var createMatch = function(player1Name,player2Name,result){ 
	return {player1Name:player1Name, player2Name:player2Name, result:result}
};

// NORMAL WAY
var Match = function(player1Name,player2Name,result){ 
	// creates a new object
	// this = new object
	this.player1Name = player1Name;
	this.player2Name = player2Name;
	this.result = result;
	// returns this
	// acts equivalently as first example.
	this.winner = function(){
		return this.result > 0.5 ? this.player2Name : this.player1Name;
	} // this may be a good idea in terms of data hiding but dont worry now.
};

// IN MOST CASES, IT IS BETTER TO MAKE THE METHODS OF THE OBJECT OUTSIDE IN THE FOLLOWING WAY USING PROTOTYPE
// THAT WAY EACHOBJECT INSTANCE REFERS TO THE SAME METHODS RATHER THAN MAKING NEW ONES
Match.prototype = {
	toString: function(){
		return "Hi";
	}


};


var matches = [];
//matches.push(createMatch("rishi","mary",0));
matches.push(new Match("tom","allison",0));

console.log(matches[0].winner());
console.log(matches[0].toString());

var tournamentFunctions = {
	getPlayers: function(matches){
		var players = [];
		matches.forEach(function(match){
			if (!contains(players, match.player1Name)) {
				players.push(match.player1Name);
			}
			if (!contains(players, match.player2Name)) {
				players.push(match.player2Name);
			}
		});
		return players;
	},
	rankPlayers: function(matches){
		var players = this.getPlayers(matches);
	}
};


function newRatings(player1Rating,player2Rating,kValue,result,shouldRound) {
	var shouldRound=False
	var kValue=32;
	// Assign actual results to players.
	var player1Result = result;
	var player2Result = 1 - result;

	// Calculate expectated results given ratings before game.
	var player1Expectation = 1 / (1+Math.pow(10,((player2Rating - player1Rating)/400)));
	var player2Expectation = 1 / (1+Math.pow(10,((player1Rating - player2Rating)/400)));

	// Calculate new rating
	var player1NewRating = player1Rating + (kValue*(player1Result - player1Expeectation));
	var player2NewRating = player2Rating + (kValue*(player2Result - player2Expeectation));

	// Handle Optional Rounding
	if (shouldRound) {
		player1NewRating = round(player1NewRating);
		player2NewRating = round(player2NewRating);	
	}

	// Create and return object
	var newScores = {'player1':player1NewRating,'player2':player2NewRating}; 
	return newScores
}

new Match("tom","allison",1);
console.log(matches);

//new Player("Rishi", 1800);

/*
console.log(fn1);
console.log(fn2);

var fn1 = function(){};
function fn2(){};

console.log(fn1);
console.log(fn2);
*/





// newRatings(1600,1600,30,1)
console.log("Hello!")
console.log(Match.prototype);