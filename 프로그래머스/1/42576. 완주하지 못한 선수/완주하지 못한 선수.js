function solution(participant, completion) {
    var answer = '';
    var map = new Map();
    
    participant.forEach((e, idx) => {
        if (map.has(e)) {
            var prev = map.get(e);
            map.set(e, prev + 1);
        } else {
            map.set(e, 1);
        }
    });
    
    completion.forEach((e, idx) => {
        if (map.has(e)) {
            var prev = map.get(e);
            map.set(e, prev - 1);
        }
    });
    
    for ([key, value] of map) {
        if (value === 1) {
            answer = key;
        }
    }
    
    return answer;
}