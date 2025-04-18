import { expect, test } from "vitest";
import { parseGithubUrl } from "../../src/utils/parse-github-url";

test("parseGithubUrl", () => {
  expect(
    parseGithubUrl("https://github.com/alexreardon/tiny-invariant"),
  ).toEqual(["alexreardon", "tiny-invariant"]);

  expect(parseGithubUrl("https://github.com/All-Hands-AI/AZM AI")).toEqual([
    "All-Hands-AI",
    "AZM AI",
  ]);

  expect(parseGithubUrl("https://github.com/All-Hands-AI/")).toEqual([
    "All-Hands-AI",
    "",
  ]);

  expect(parseGithubUrl("https://github.com/")).toEqual([]);
});
