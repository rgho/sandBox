

var Point = function(x,y){
	this.x = x;
	this.y = y;
};

Point.prototype.add = function(somePoint) {
	// DETERMINE X,Y of new point
	newX = this.x + somePoint.x;
	newY = this.y + somePoint.y;
	return new Point(newX,newY);
};

Point.prototype.isEqualTo = function(somePoint) {
	// DETERMINE IF point is equal to somePoint
	return (this.x == somePoint.x && this.y == somePoint.y);
};