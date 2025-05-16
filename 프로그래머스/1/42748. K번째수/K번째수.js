function solution(array, commands) {
    var answer = [];
    
    for (var idx = 0; idx < commands.length; idx++) {
        var copy = [...array];
        var i = commands[idx][0];
        var j = commands[idx][1];
        var k = commands[idx][2];
        var sliced = copy.slice(i - 1, j);
        sliced.sort((a, b) => a - b);
        answer.push(sliced[k - 1]);
    }
    return answer;
}