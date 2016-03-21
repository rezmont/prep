def make_longest_stack(h, boxes, last_box_dim):
    if len(boxes) == 0:
        return h

    l_w, l_h, l_d = last_box_dim
    possible_top_boxes = []
    if l_w != -1:
        for box in boxes:
            c_w, c_h, c_d = box
            if c_w < l_w and c_h < l_h and c_d < l_d:
                possible_top_boxes.append(box)
    else:
        possible_top_boxes = boxes
    
    h_max = 0
    for i, box in enumerate(possible_top_boxes):
        h_ret = box[1] + make_longest_stack(h, possible_top_boxes[:i]+possible_top_boxes[i+1:], box)
        if h_max < h_ret:
            h_max = h_ret
        
    return h_max


boxes = [(100, 100, 100), (200, 1000000, 1000), (20, 20, 10)]
h = make_longest_stack(0, boxes, (-1, -1, -1))
print h
