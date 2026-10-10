
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>按鈕與對話框</title>

  <style>
    body {
      font-family: "Microsoft JhengHei", sans-serif;
      background: #f5f7fb;
      display: grid;
      place-items: center;
      min-height: 100vh;
      margin: 0;
    }

    .panel {
      background: white;
      padding: 40px;
      border-radius: 16px;
      text-align: center;
      box-shadow: 0 8px 30px #15284b1a;
    }

    button {
      border: 0;
      border-radius: 8px;
      padding: 12px 20px;
      cursor: pointer;
      font-size: 16px;
    }

    button:hover {
      opacity: 0.8;
    }

    .danger {
      background: #c62828;
      color: white;
    }

    .secondary {
      background: #e9eef5;
      color: #24334b;
    }

    dialog {
      border: 0;
      border-radius: 14px;
      padding: 28px;
      max-width: 360px;
      box-shadow: 0 20px 50px #0003;
    }

    dialog::backdrop {
      background: #0006;
    }

    .actions {
      display: flex;
      justify-content: flex-end;
      gap: 10px;
      margin-top: 25px;
    }

    #status {
      color: #227343;
    }
  </style>
</head>

<body>
  <main class="panel">
    <h1>按鈕與對話框</h1>
    <p>點擊按鈕，體驗確認流程。</p>

    <button class="danger" id="deleteBtn">
      刪除資料
    </button>

    <p id="status" role="status"></p>
  </main>

  <dialog id="confirmDialog">
    <h2>確認刪除</h2>
    <p>確定要刪除資料嗎？</p>

    <div class="actions">
      <button class="secondary" id="cancelBtn">
        取消
      </button>

      <button class="danger" id="confirmBtn">
        確認刪除
      </button>
    </div>
  </dialog>

  <script>
    const dialog = document.querySelector("#confirmDialog");

    // 點擊刪除按鈕，開啟對話框
    document.querySelector("#deleteBtn")
      .addEventListener("click", () => {
        dialog.showModal();
      });

    // 點擊取消，關閉對話框
    document.querySelector("#cancelBtn")
      .addEventListener("click", () => {
        dialog.close();
      });

    // 點擊確認，顯示結果
    document.querySelector("#confirmBtn")
      .addEventListener("click", () => {
        dialog.close();

        document.querySelector("#status").textContent =
          "已確認刪除（示範，不會真的刪除資料）";
      });
  </script>
</body>
</html>
