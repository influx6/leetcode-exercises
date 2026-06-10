const test = require("node:test");
const assert = require("node:assert");
const util = require("util");

const { describe, it } = test;

class IPRateLimiter {
  constructor(time_limit) {
    this.time_limit = time_limit;
  }

  *filter(requests) {
    if (!requests) return [];

    const results = [];
    const identified = {};
    for (let index in requests) {
      const request = requests[index];
      const parts = request.split(/\s/, -1);
      if (parts.length != 3) continue;

      const [request_id, request_ip, timestamp_str] = parts;
      if (
        this.is_empty_string(request_id) ||
        this.is_empty_string(request_ip) ||
        this.is_empty_string(timestamp_str) ||
        this.not_valid_ip(request_ip)
      ) {
        continue;
      }

      const timestamp = parseInt(timestamp_str, 10);
      if (isNaN(timestamp)) continue;

      if (!(request_ip in identified)) {
        identified[request_ip] = timestamp;
        yield request;
        continue;
      }

      const previous_timestamp = identified[request_ip];
      // ensure we are dealing with absolute numbers, sign does not matter here
      const diff_in_timestamp = Math.abs(
        Math.abs(previous_timestamp) - Math.abs(timestamp)
      );
      if (diff_in_timestamp > 0 && diff_in_timestamp >= this.time_limit) {
        identified[request_ip] = timestamp;
        yield request;
        continue;
      }
    }
  }

  is_empty_string(value) {
    if (!value || value.trim().length == 0) return true;
    return false;
  }

  not_valid_ip(request_ip) {
    const found = request_ip.split(".").find((part) => {
      const part_number = parseInt(part, 10);
      if (isNaN(part_number) || 0 > part_number || part_number > 255) {
        return true;
      }
      return false;
    });
    return found != undefined || found != null;
  }
}

// Mocha test suite
describe("instance.filter", () => {
  it("should handle handle cases when limit is 10seconds but with one greater than 10seconds", () => {
    const instance = new IPRateLimiter(10);
    const input = [
      "req1 192.168.1.1 1625098765",
      "req2 192.168.1.2 1625098766",
      "req3 192.168.1.1 1625098767",
      "req4 192.168.1.1 1625098777",
    ];
    const expected = [
      "req1 192.168.1.1 1625098765",
      "req2 192.168.1.2 1625098766",
      "req4 192.168.1.1 1625098777",
    ];
    assert.deepStrictEqual(Array.from(instance.filter(input)), expected);
  });

  it("should handle handle cases when limit is 10seconds", () => {
    const instance = new IPRateLimiter(10);
    const input = [
      "req1 192.168.1.1 1625098765",
      "req2 192.168.1.2 1625098766",
      "req3 192.168.1.1 1625098767",
    ];
    const expected = [
      "req1 192.168.1.1 1625098765",
      "req2 192.168.1.2 1625098766",
    ];
    assert.deepStrictEqual(Array.from(instance.filter(input)), expected);
  });

  // Example 1: Basic Case with No Violations
  it("should handle basic case with no violations", () => {
    const instance = new IPRateLimiter(1);
    const input = [
      "req1 192.168.1.1 1625098765",
      "req2 192.168.1.2 1625098766",
      "req3 192.168.1.1 1625098767",
    ];
    const expected = [
      "req1 192.168.1.1 1625098765",
      "req2 192.168.1.2 1625098766",
      "req3 192.168.1.1 1625098767",
    ];
    assert.deepStrictEqual(Array.from(instance.filter(input)), expected);
  });

  // Example 2: Multiple Requests in the Same Second
  it("should filter out multiple requests from same IP in same second", () => {
    const instance = new IPRateLimiter(1);
    const input = [
      "req1 192.168.1.1 1625098765",
      "req2 192.168.1.1 1625098765",
      "req3 192.168.1.1 1625098766",
      "req4 192.168.1.2 1625098765",
    ];
    const expected = [
      "req1 192.168.1.1 1625098765",
      "req3 192.168.1.1 1625098766",
      "req4 192.168.1.2 1625098765",
    ];
    assert.deepStrictEqual(Array.from(instance.filter(input)), expected);
  });

  // Example 3: Empty Input
  it("should handle empty input", () => {
    const instance = new IPRateLimiter(1);

    const input = [];
    const expected = [];
    assert.deepStrictEqual(Array.from(instance.filter(input)), expected);
  });

  // Example 4: Single Request
  it("should handle single request", () => {
    const instance = new IPRateLimiter(1);
    const input = ["req1 192.168.1.1 1625098765"];
    const expected = ["req1 192.168.1.1 1625098765"];
    assert.deepStrictEqual(Array.from(instance.filter(input)), expected);
  });

  // Example 5: Unsorted Timestamps
  it("should handle unsorted timestamps", () => {
    const instance = new IPRateLimiter(1);
    const input = [
      "req1 192.168.1.1 1625098766",
      "req2 192.168.1.1 1625098765",
      "req3 192.168.1.2 1625098765",
      "req4 192.168.1.1 1625098765",
    ];
    const expected = [
      "req1 192.168.1.1 1625098766",
      "req2 192.168.1.1 1625098765",
      "req3 192.168.1.2 1625098765",
    ];
    assert.deepStrictEqual(Array.from(instance.filter(input)), expected);
  });

  // Example 6: Large Timestamps
  it("should handle large timestamps", () => {
    const instance = new IPRateLimiter(1);
    const input = [
      "req1 192.168.1.1 9999999999",
      "req2 192.168.1.1 9999999999",
      "req3 192.168.1.1 10000000000",
    ];
    const expected = [
      "req1 192.168.1.1 9999999999",
      "req3 192.168.1.1 10000000000",
    ];
    assert.deepStrictEqual(Array.from(instance.filter(input)), expected);
  });

  // Example 7: Multiple IPs with Overlapping Timestamps
  it("should handle multiple IPs with overlapping timestamps", () => {
    const instance = new IPRateLimiter(1);
    const input = [
      "req1 192.168.1.1 1625098765",
      "req2 192.168.1.2 1625098765",
      "req3 192.168.1.1 1625098765",
      "req4 192.168.1.2 1625098765",
      "req5 192.168.1.3 1625098765",
    ];
    const expected = [
      "req1 192.168.1.1 1625098765",
      "req2 192.168.1.2 1625098765",
      "req5 192.168.1.3 1625098765",
    ];
    assert.deepStrictEqual(Array.from(instance.filter(input)), expected);
  });

  // Edge Case 1: Malformed Input
  it("should skip malformed input", () => {
    const instance = new IPRateLimiter(1);
    const input = [
      "req1 192.168.1.1 1625098765",
      "req2 192.168.1.1", // Missing timestamp
      "req3 192.168.1.1 abc", // Invalid timestamp
      "req4 256.256.256.256 1625098765", // Invalid IP
      "req5 192.168.1.2 1625098765",
    ];
    const expected = [
      "req1 192.168.1.1 1625098765",
      "req5 192.168.1.2 1625098765",
    ];
    assert.deepStrictEqual(Array.from(instance.filter(input)), expected);
  });

  // Edge Case 2: Negative Timestamps
  it("should handle negative timestamps", () => {
    const instance = new IPRateLimiter(1);
    const input = [
      "req1 192.168.1.1 -1625098765",
      "req2 192.168.1.1 -1625098765",
      "req3 192.168.1.1 -1625098764",
    ];
    const expected = [
      "req1 192.168.1.1 -1625098765",
      "req3 192.168.1.1 -1625098764",
    ];
    assert.deepStrictEqual(Array.from(instance.filter(input)), expected);
  });

  // Edge Case 3: Duplicate Request IDs
  it("should handle duplicate request IDs", () => {
    const instance = new IPRateLimiter(1);
    const input = [
      "req1 192.168.1.1 1625098765",
      "req1 192.168.1.1 1625098765", // Same ID, same IP, same second
      "req1 192.168.1.1 1625098766", // Same ID, same IP, different second
      "req1 192.168.1.2 1625098765", // Same ID, different IP
    ];
    const expected = [
      "req1 192.168.1.1 1625098765",
      "req1 192.168.1.1 1625098766",
      "req1 192.168.1.2 1625098765",
    ];
    assert.deepStrictEqual(Array.from(instance.filter(input)), expected);
  });

  // Edge Case 4: Large Input (Performance Test)
  it("should handle large input efficiently", () => {
    const instance = new IPRateLimiter(1);

    const input = [];
    const expected = [];
    // Generate 1000 requests: 500 IPs with 2 requests each, same second
    for (let i = 0; i < 500; i++) {
      input.push(`req${i * 2 + 1} 192.168.1.${i + 1} 1625098765`);
      input.push(`req${i * 2 + 2} 192.168.1.${i + 1} 1625098765`);
      if (i + 1 <= 255) {
        expected.push(`req${i * 2 + 1} 192.168.1.${i + 1} 1625098765`);
      }
    }
    const result = Array.from(instance.filter(input));
    assert.deepStrictEqual(result, expected);
  });
});
