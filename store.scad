$fn = 50;

// Parameters
shelf_length = 100;
shelf_width = 40;
shelf_height = 150;
aisle_width = 60;

store_length = 800;
store_width = 500;
store_height = 300;

entrance_width = 80;
checkout_length = 200;
wall_thickness = 5;
stairs_width = 80;

// Shelf module
module shelf() {
    color("brown") {
        cube([shelf_length, shelf_width, shelf_height]);
    }
}

// Aisle module (consisting of shelves on both sides)
module aisle() {
    shelf();
    translate([0, shelf_width + aisle_width, 0])
    shelf();
}

// Entrance area
module entrance() {
    color("lightgray") {
        cube([entrance_width, wall_thickness, store_height]); // Entrance door
    }
}

// Checkout area
module checkout() {
    color("green") {
        cube([checkout_length, entrance_width, 40]); // Checkout counter
    }
}

// Staircase
module staircase() {
    for (i = [0:store_height/10 - 1]) {
        translate([0, i*10, i*10]) {
            cube([stairs_width, 10, 10]);
        }
    }
}

// Store layout
module store() {
    // Store perimeter
    color("gray") {
        difference() {
            cube([store_length, store_width, store_height]);
            translate([wall_thickness, wall_thickness, 0])
            cube([store_length - 2*wall_thickness, store_width - 2*wall_thickness, store_height]);
        }
    }

    // Entrances
    entrance();
    translate([store_length - entrance_width, 0, 0]) entrance();

    // Aisles with shelves on the first floor
    for (i = [0:5]) {
        translate([(i + 1) * (shelf_length + aisle_width), entrance_width, wall_thickness]) {
            aisle();
        }
    }

    // Checkout areas
    translate([entrance_width, store_width - entrance_width - wall_thickness, wall_thickness]) checkout();
    translate([store_length - entrance_width - checkout_length, wall_thickness, wall_thickness]) checkout();

    // Staircases
    translate([store_length/2, store_width - 2*stairs_width, wall_thickness]) staircase();
    translate([store_length/2 - stairs_width, 2*stairs_width, wall_thickness]) staircase();
}

store();
    