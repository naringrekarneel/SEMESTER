<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Topic 2: Padding in CNNs</title>
  <!-- MathJax for rendering LaTeX formulas -->
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <style>
    :root {
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text-main: #1e293b;
      --text-muted: #64748b;
      --primary: #2563eb;
      --primary-light: #eff6ff;
      --border: #e2e8f0;
      --code-bg: #0f172a;
      --code-text: #38bdf8;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.65;
      color: var(--text-main);
      background-color: var(--bg);
      margin: 0;
      padding: 2rem 1rem;
    }

    .container {
      max-width: 840px;
      margin: 0 auto;
      background: var(--card-bg);
      padding: 2.5rem;
      border-radius: 12px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      border: 1px solid var(--border);
    }

    h1 {
      font-size: 2rem;
      border-bottom: 2px solid var(--primary);
      padding-bottom: 0.5rem;
      color: #0f172a;
      margin-top: 0;
    }

    h2 {
      font-size: 1.35rem;
      color: #1e3a8a;
      margin-top: 2rem;
      margin-bottom: 0.75rem;
    }

    h3 {
      font-size: 1.1rem;
      color: #334155;
      margin-top: 1.25rem;
    }

    p, li {
      color: var(--text-main);
    }

    ul, ol {
      padding-left: 1.5rem;
    }

    li {
      margin-bottom: 0.4rem;
    }

    hr {
      border: 0;
      height: 1px;
      background: var(--border);
      margin: 2rem 0;
    }

    pre {
      background: var(--code-bg);
      color: var(--code-text);
      padding: 1rem;
      border-radius: 8px;
      overflow-x: auto;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 0.95rem;
      line-height: 1.4;
    }

    .math-block {
      background: #f1f5f9;
      border-left: 4px solid var(--primary);
      padding: 0.75rem 1rem;
      margin: 1rem 0;
      border-radius: 0 6px 6px 0;
      overflow-x: auto;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin: 1.25rem 0;
    }

    th, td {
      border: 1px solid var(--border);
      padding: 0.75rem 1rem;
      text-align: left;
    }

    th {
      background-color: #f8fafc;
      font-weight: 600;
      color: #0f172a;
    }

    tr:nth-child(even) {
      background-color: #fdfdfd;
    }

    blockquote {
      background: var(--primary-light);
      border-left: 4px solid var(--primary);
      margin: 1rem 0;
      padding: 0.75rem 1rem;
      color: #1e40af;
      font-weight: 500;
      border-radius: 0 6px 6px 0;
    }

    .box-formula {
      border: 2px solid var(--primary);
      border-radius: 8px;
      padding: 1rem;
      background: #ffffff;
      text-align: center;
      margin: 1.5rem 0;
    }

    .questions-card {
      background: #fafaf9;
      border: 1px solid #d6d3d1;
      border-radius: 8px;
      padding: 1.25rem;
      margin-top: 1.5rem;
    }
  </style>
</head>
<body>

  <main class="container">
    <header>
      <h1>Topic 2: Padding</h1>
      <p>Padding is the next piece of the CNN puzzle. It solves an important problem caused by convolution: the image gets smaller every time we apply a filter.</p>
    </header>

    <hr>

    <section>
      <h2>1. Padding — ELI5</h2>
      <p>Imagine you have a photo and you're putting a frame around it before applying a filter.</p>
      <p>That extra border is <strong>padding</strong>.</p>
      <p>Instead of letting the convolution filter operate only inside the original image, we add extra pixels around the edges.</p>
      <p>Usually, these added pixels are zeros, so this is called <strong>zero padding</strong>.</p>
      
      <p><strong>Why do we need it?</strong></p>
      <ul>
        <li><strong>Without padding:</strong> Input &rarr; Convolution &rarr; Smaller output</li>
        <li><strong>With padding:</strong> Input &rarr; Padding &rarr; Convolution &rarr; Same-size or controlled output</li>
      </ul>
    </section>

    <hr>

    <section>
      <h2>2. Why is padding necessary?</h2>
      <p>There are two major reasons.</p>

      <h3>Reason 1: Prevent excessive reduction in image size</h3>
      <p>Suppose:</p>
      <ul>
        <li>Input = \(5 \times 5\)</li>
        <li>Kernel = \(3 \times 3\)</li>
        <li>Stride = 1</li>
        <li>Padding = 0</li>
      </ul>

      <div class="math-block">
        \[
        O = \frac{5 - 3 + 2(0)}{1} + 1 = 3
        \]
      </div>

      <p>So: <strong>\(5 \times 5 \rightarrow 3 \times 3\)</strong></p>
      <p>If we repeatedly perform convolution, the feature map becomes smaller and smaller.</p>

      <h3>Reason 2: Preserve information at the edges</h3>
      <p>This is actually a big deal.</p>
      <p>Consider a filter scanning an image:</p>
      <ul>
        <li>Pixels in the <strong>center</strong> participate in many convolution operations.</li>
        <li>Pixels near the <strong>corners and edges</strong> participate in fewer operations.</li>
      </ul>
      <p>Without padding, information near the boundaries can be underrepresented. Padding gives those boundary pixels more opportunities to contribute.</p>
    </section>

    <hr>

    <section>
      <h2>3. Types of Padding</h2>
      <p>The two terms you absolutely need to know for exams are:</p>
      
      <h3>1. Valid Padding</h3>
      <p>No padding is added (\(P = 0\)).</p>
      <p>Example: \(5 \times 5 \rightarrow 3 \times 3\)</p>
      <p><em>So VALID = no padding.</em></p>

      <h3>2. Same Padding</h3>
      <p>Padding is added so that the output spatial dimensions remain the same as the input when \(S = 1\).</p>
      <p>Example: \(5 \times 5 \rightarrow 5 \times 5\)</p>
      <p><em>So SAME = preserve spatial size when stride is 1.</em></p>
    </section>

    <hr>

    <section>
      <h2>4. Visual Intuition</h2>
      <p>Suppose our image is:</p>
      <pre>1 2 3
4 5 6
7 8 9</pre>

      <p>With zero padding of 1:</p>
      <pre>0 0 0 0 0
0 1 2 3 0
0 4 5 6 0
0 7 8 9 0
0 0 0 0 0</pre>

      <p>The original \(3 \times 3\) becomes \(5 \times 5\) before convolution.</p>
    </section>

    <hr>

    <section>
      <h2>5. How much padding is required?</h2>
      <p>For a common case where <strong>Kernel size is odd</strong>, <strong>Stride = 1</strong>, and <strong>Same padding</strong> is desired:</p>
      
      <div class="math-block">
        \[
        P = \frac{K - 1}{2}
        \]
      </div>

      <ul>
        <li>For a \(3 \times 3\) kernel: \(P = \frac{3 - 1}{2} = 1\) (add 1 layer of zeros)</li>
        <li>For a \(5 \times 5\) kernel: \(P = \frac{5 - 1}{2} = 2\) (add 2 layers of zeros)</li>
      </ul>
    </section>

    <hr>

    <section>
      <h2>6. Output-Size Formula</h2>
      <p>This is very important for exams and numerical questions:</p>
      
      <div class="math-block">
        \[
        O = \left\lfloor \frac{N + 2P - K}{S} \right\rfloor + 1
        \]
      </div>

      <table>
        <thead>
          <tr>
            <th>Symbol</th>
            <th>Meaning</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>\(N\)</td>
            <td>Input size</td>
          </tr>
          <tr>
            <td>\(K\)</td>
            <td>Kernel size</td>
          </tr>
          <tr>
            <td>\(P\)</td>
            <td>Padding</td>
          </tr>
          <tr>
            <td>\(S\)</td>
            <td>Stride</td>
          </tr>
          <tr>
            <td>\(O\)</td>
            <td>Output size</td>
          </tr>
        </tbody>
      </table>
    </section>

    <hr>

    <section>
      <h2>7. Worked Example 1 — No Padding</h2>
      <p><strong>Given:</strong> Input = \(7 \times 7\), Kernel = \(3 \times 3\), Padding = 0, Stride = 1</p>
      
      <div class="math-block">
        \[
        O = \frac{7 + 2(0) - 3}{1} + 1 = 5
        \]
      </div>
      <p>Therefore: <strong>\(7 \times 7 \rightarrow 5 \times 5\)</strong> (Valid convolution).</p>
    </section>

    <hr>

    <section>
      <h2>8. Worked Example 2 — Same Padding</h2>
      <p><strong>Given:</strong> Input = \(7 \times 7\), Kernel = \(3 \times 3\), Padding = 1, Stride = 1</p>
      
      <div class="math-block">
        \[
        O = \frac{7 + 2(1) - 3}{1} + 1 = 7
        \]
      </div>
      <p>Therefore: <strong>\(7 \times 7 \rightarrow 7 \times 7\)</strong> (Spatial dimensions preserved).</p>
    </section>

    <hr>

    <section>
      <h2>9. Worked Example 3 — Understanding the Difference</h2>
      <p>Suppose: \(N = 32,\quad K = 3,\quad S = 1\)</p>

      <p><strong>Valid Padding (\(P = 0\)):</strong></p>
      <div class="math-block">
        \[
        O = \frac{32 - 3}{1} + 1 = 30 \implies 30 \times 30
        \]
      </div>

      <p><strong>Same Padding (\(P = 1\)):</strong></p>
      <div class="math-block">
        \[
        O = \frac{32 + 2 - 3}{1} + 1 = 32 \implies 32 \times 32
        \]
      </div>

      <table>
        <thead>
          <tr>
            <th>Padding</th>
            <th>Input</th>
            <th>Output</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Valid</td>
            <td>\(32 \times 32\)</td>
            <td>\(30 \times 30\)</td>
          </tr>
          <tr>
            <td>Same</td>
            <td>\(32 \times 32\)</td>
            <td>\(32 \times 32\)</td>
          </tr>
        </tbody>
      </table>
    </section>

    <hr>

    <section>
      <h2>10. Padding and Edge Information</h2>
      <p>A common theoretical exam question.</p>
      <p><strong>Without padding:</strong></p>
      <pre>[ EDGE ][ EDGE ][ EDGE ]
[      ][CENTER][      ]
[ EDGE ][ EDGE ][ EDGE ]</pre>
      <p>The filter cannot be centered around an edge pixel without moving outside the boundary of the image.</p>

      <p><strong>With padding:</strong></p>
      <pre>0  0  0  0  0
0  A  B  C  0
0  D  E  F  0
0  G  H  I  0
0  0  0  0  0</pre>
      <p>Now the filter can center directly over boundary pixels (like A, B, C) while keeping its full footprint populated.</p>
    </section>

    <hr>

    <section>
      <h2>11. Padding in CNN Architecture</h2>
      <p>A typical pipeline:</p>
      <pre>Input Image &rarr; Convolution &rarr; ReLU &rarr; Convolution &rarr; ReLU &rarr; Pooling &rarr; ...</pre>

      <p>Using <em>same padding</em> in convolution layers maintains spatial dimensions prior to pooling:</p>
      <div class="math-block">
        \[
        32 \times 32 \xrightarrow{\text{Conv (Same)}} 32 \times 32 \xrightarrow{\text{Pool}} 16 \times 16
        \]
      </div>
      <p>Convolution extracts feature representations without shrinkage; pooling intentionally controls downsampling. This modularity makes architectures easier to plan.</p>
    </section>

    <hr>

    <section>
      <h2>12. Exam Answer Summary — Padding</h2>
      <p>Structure your answer: <strong>Definition &rarr; Need &rarr; Types &rarr; Formula &rarr; Example &rarr; Advantages</strong></p>
      <ul>
        <li><strong>Definition:</strong> Padding adds extra pixels around the perimeter of the input feature map (zero padding being the standard).</li>
        <li><strong>Valid Padding:</strong> \(P = 0\); spatial dimension contracts.</li>
        <li><strong>Same Padding:</strong> Retains input dimensions when \(S = 1\).</li>
        <li><strong>Padding Formula:</strong> \(P = \frac{K - 1}{2}\) (for odd \(K\), \(S = 1\)).</li>
        <li><strong>Output Formula:</strong> \(O = \lfloor \frac{N + 2P - K}{S} \rfloor + 1\).</li>
      </ul>
    </section>

    <hr>

    <section>
      <h2>Quick Revision</h2>
      <blockquote>VALID &rarr; No padding &rarr; Smaller output</blockquote>
      <blockquote>SAME &rarr; Padding added &rarr; Same spatial size when \(S = 1\)</blockquote>

      <div class="box-formula">
        <strong>The Golden Formula:</strong>
        \[
        \bbox[8px, border: 1.5px solid #2563eb]{O = \left\lfloor \frac{N + 2P - K}{S} \right\rfloor + 1}
        \]
      </div>
    </section>

    <hr>

    <section class="questions-card">
      <h2>Active Learning</h2>

      <h3>Conceptual</h3>
      <ol>
        <li>What is the main purpose of padding in CNNs?</li>
        <li>What is the difference between VALID and SAME padding?</li>
        <li>Why are edge pixels more likely to lose influence without padding?</li>
      </ol>

      <h3>Numerical Problem</h3>
      <p><strong>Q4:</strong> An input image is \(28 \times 28\). A \(5 \times 5\) kernel is used with stride \(1\) and padding \(2\).</p>
      <p>Calculate the output size using the output-size formula.</p>
    </section>
  </main>

</body>
</html>

