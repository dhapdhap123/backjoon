const [A, B, C] = [BigInt(10192847), BigInt(100000), BigInt(12)];
// console.log(A ** 11 % 12);
// console.log(A ** 11);

// const [A, B, C] = input[0].split(' ').map(BigInt);

// const fs = require("fs");
// let [A, B, C] = fs.readFileSync("/dev/stdin").toString().split(" ").map(BigInt);

const solve = (power) => {
  // B가 1이면 곱하나마나니까 바로 A%C 출력
  if (power === 1n) {
    return A % C;
  }
  // B를 2로 나눈 값을 입력하여 함수를 재귀적으로 호출한다.
  const half = solve(power / 2n) % C;

  // B를 2로 나눈 나머지가 1이면(홀수면) ((A^(B / 2) % C) * (A^(B / 2) % C) * (A % C)) % C 를 적용한다.
  if (power % 2n) {
    return (half * half * (A % C)) % C;
  }

  // B가 짝수면 ((A^(B / 2) % C) * (A^(B / 2) % C)) % C 를 적용한다.
  return (half * half) % C;
};

console.log(solve(B).toString());
