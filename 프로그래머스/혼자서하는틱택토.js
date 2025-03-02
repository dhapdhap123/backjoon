function solution(board) {
  const oArr = [];
  const xArr = [];

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < 3; j++) {
      if (board[i][j] === "O") {
        oArr.push([i, j]);
      } else if (board[i][j] === "X") {
        xArr.push([i, j]);
      }
    }
  }
  if (xArr.length > oArr.length) return 0;
  else if (oArr.length - xArr.length > 1) return 0;

  const vec = [
    [1, 0],
    [0, 1],
    [1, 1],
    [1, -1],
  ];

  //     3x3 9개의 점에서 각각 vec에서 하나 골라서 접근
  const oBingoArr = [];
  const xBingoArr = [];
  function dfs(i, j, arr, v, startStr) {
    // console.log(i, j);
    // console.log(board[i][j])
    if (i < 0 || i >= 3 || j < 0 || j >= 3 || board[i][j] !== startStr) return;

    arr.push([i, j]);

    if (arr.length === 3) {
      if (startStr === "O") {
        oBingoArr.push(arr);
        return;
      } else if (startStr === "X") {
        xBingoArr.push(arr);
        return;
      }
    }
    return dfs(i + v[0], j + v[1], arr, v, startStr);
  }

  const checkList = [
    [0, 0],
    [0, 1],
    [0, 2],
    [1, 0],
    [2, 0],
  ];
  for (let k of checkList) {
    for (let v of vec) {
      console.log(k[0], k[1], v, "에 대해 실행, 시작: ", board[k[0]][k[1]]);
      dfs(k[0], k[1], [], v, board[k[0]][k[1]]);
    }
  }

  console.log(oBingoArr, xBingoArr);
  if (xBingoArr.length >= 1 && oBingoArr.length >= 1) return 0;
  if (xBingoArr.length >= 2) {
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        if (
          xBingoArr[0][i][0] === xBingoArr[1][j][0] &&
          xBingoArr[0][i][1] === xBingoArr[1][j][1]
        ) {
          return 1;
        }
      }
    }
  } else if (oBingoArr.length >= 2) {
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        if (
          oBingoArr[0][i][0] === oBingoArr[1][j][0] &&
          oBingoArr[0][i][1] === oBingoArr[1][j][1]
        ) {
          return 1;
        }
      }
    }
  }
  //   빙고가 나오면 더 둘 수 없음
  // ex) X 3개, O 4개. Bingo => 0
  // oBingoArr가 1 OOO XXX
  if (xBingoArr.length === 1 && oArr.length > xArr.length) return 0;
  if (oBingoArr.length === 1 && xArr.length >= oArr.length) return 0;
  return 1;
}
console.log(solution(["OOO", "OXX", "OXX"]));
