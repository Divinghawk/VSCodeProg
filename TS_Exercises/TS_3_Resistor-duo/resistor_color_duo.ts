const resistances = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
];

export const decodedValue = ([first, last]: Array<string>) => {
    // throw new Error('Remove this statement and implement this function')
    const value = [first, last].reduce(
        (prev, color) => prev + resistances.indexOf(color), ""
    );

    return Number(value);
  }