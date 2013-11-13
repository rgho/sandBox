

tom = new RatedPlayer("Tom", 1600);
console.log(tom.rating);
alan = new RatedPlayer("Alan", 1800);
blah = new Match(tom,alan,1);
console.log(tom.rating);


var RatedPlayer = function(id,rating){
	this.rating = rating;
	this.id = id;
};

RatedPlayer.prototype.updateRating = function(newRating){
	this.rating = newRating;
};

var Match = function(player1,player2,result){
	newRatings = calcNewRatings(player1.rating,player2.rating,32,1,0);
	player1.updateRating(newRatings.player1);
	player2.updateRating(newRatings.player2);
};


function calcNewRatings(player1Rating,player2Rating,kValue,result,shouldRound) {
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
};
