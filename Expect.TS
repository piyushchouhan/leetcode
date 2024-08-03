type ToBeOrNotToBe = {
    toBe: (val: any) => boolean;
    notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
    return {
        toBe: (expected) => {
            if (val === expected) {
                return true;
            } else {
                throw new Error("Not Equal");
            }
        },
        notToBe: (expected) => {
            if (val !== expected) {
                return true;
            } else {
                throw new Error("Equal");
            }
        }
    };
}

// Example usage:
try {
    console.log(expect(5).toBe(5)); // true
} catch (e) {
    console.error(e.message); // Not Equal (if the values are not equal)
}

try {
    console.log(expect(5).notToBe(4)); // true
} catch (e) {
    console.error(e.message); // Equal (if the values are equal)
}
