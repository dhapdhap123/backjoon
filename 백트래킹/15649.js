// var fs = require("fs");
// var input = fs.readFileSync("/dev/stdin").toString().trim().split();

const N = 6;
const array = [1, 2, 3, 4, 5, 6];
const operators = [2, 1, 1, 1];
const operatorArr = ["+", "-", "*", "/"];

// 연산자 선택 경우의 수
function permutation(array, length) {
  const result = [];

  const visited = new Array(4).fill(0);
  function dfs(cnt) {
    if (current.length === n) {
      result.push([...current]);
      return;
    }

    for (let i = 0; i < arr.length; i++) {
      if (!visited[i]) {
        //방문 여부 체크 후
        visited[i] = true; //방문처리
        current.push(arr[i]);
        dfs(current);
        current.pop();
        visited[i] = false; //다음 반복을 위해 미방문 처리
      }
    }
  }
}
