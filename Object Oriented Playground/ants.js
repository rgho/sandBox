
// A NEW POINT OBJECT.
var Point = function(x,y){
	this.x = x;
	this.y = y;
};

Point.prototype.add = function(anotherPoint) {
	// DETERMINE X,Y of new point
	newX = this.x + anotherPoint.x;
	newY = this.y + anotherPoint.y;
	return new Point(newX,newY);
};

Point.prototype.isEqualTo = function(anotherPoint) {
	// DETERMINE IF point is equal to somePoint
	return (this.x == anotherPoint.x && this.y == anotherPoint.y);
};

console.log((new Point(3, 1)).add(new Point(2, 4)));


// GRID OBJECT
var Grid = function(height,width){
	this.width = width;
	this.height = height;
	this.cells = new Array(width*height);
}

Grid.prototype.valueAt = function(somePoint){
	return this.cells[somePoint.x + (somePoint.y*this.width)];
};

Grid.prototype.setValueAt = function(somePoint, value){
	this.cells[somePoint.x + (somePoint.y*this.width)] = value;
};

Grid.prototype.isInside = function(somePoint){
	return point.x >= 0 && point.y >= 0 && 
		point.x < this.width &&	point.y < this.height;
};

Grid.prototype.moveValue = function(from, to){
	this.setValueAt(to,this.valueAt(from));
	this.setValueAt(from,undefined);
};

Grid.prototype.each = function(actionFunc){
	for (var y = 0; y < this.height; y++) {
		for (var x = 0; x < this.width; x++) {
			var thisPoint = new Point(x,y); // CONSTRUCT A POINT OBJ
			actionFunc(thisPoint, this.valueAt(thisPoint));
		};
	};
};

var testGrid = new Grid(3, 2);
testGrid.setValueAt(new Point(1, 0), "#");
testGrid.setValueAt(new Point(1, 1), "o");
testGrid.each(function(point, value) {
  console.log(point.x, ",", point.y, ": ", value);
});
