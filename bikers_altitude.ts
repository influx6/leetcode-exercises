function largestAltitude(gain: number[]): number {
  let maxHeight = 0;
  let currentHeight = 0;

  for (let index = 0; index < gain.length; index++) {
    currentHeight += gain[index];
    maxHeight = Math.max(maxHeight, currentHeight);
  }

  return maxHeight;
}
