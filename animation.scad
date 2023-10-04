$fn = 100; // High resolution circles

module node(radius) {
    color("blue") {
        sphere(radius);
    }
}

module edge(start, end) {
    color("black") {
        hull() {
            translate(start)
            sphere(1);
            
            translate(end)
            sphere(1);
        }
    }
}

// Layer generator
module layer(y_offset, node_count) {
    for(i = [0:node_count - 1]) {
        pos = [i*40 - 20*(node_count - 1), y_offset, 0];
        node(10);
        translate(pos)
        node(10);
        
        if (y_offset > 0) { // Don't draw edges for the first layer
            for(j = [0:node_count - 1]) {
                edge(pos, [j*40 - 20*(node_count - 1), y_offset - 150, 0]);
            }
        }
    }
}

// GNN visualization with 3 layers, each having 5, 4, and 3 nodes respectively.
layer(0, 5);
layer(150, 4);
layer(300, 3);

