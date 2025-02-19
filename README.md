# ObejectDetector 模組

## 模組說明

- 撰寫此模組目的是希望部署 YOLO 模型至不同機器時，只需要更改 `default.yaml` 內的設定，即可直接使用
- 此模組使用 ultralytics: [官方網站連結](https://docs.ultralytics.com/)
- 此模組使用 UV 套件管理 &rarr; [UV 安裝 PyTorch](https://hellowac.github.io/uv-zh-cn/guides/integration/pytorch/)

## 使用方法

- 匯入模組方式 `import ObjectDetector`
- 使用 `class ObjectDetection` 創立物件
  - Example：

    ```python
    import ObjectDetector

    myDetector = ObjectDetector.ObjectDetection()
    ```

- 將訓練好的模型，放入 model 資料夾內 (需要自己建立資料夾)

## `ObjectDetection` Attributes and Functions

### Functions

- `predict()` --- 使用載入的模型預測圖片

### Attributes

- `cls_names` --- 可讀取模型內的分類名稱
- `dst` --- 輸出資料夾路徑
