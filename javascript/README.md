## Execution Context

Khi chương trình JavaScript được chạy, **global execution context** sẽ được khởi tạo, toàn bộ code ở global sẽ được thực thi trong context này. Khi gọi/ thực thi/ chạy một function, một **function execution context** tương ứng sẽ được tạo ra và các đoạn code của function đó sẽ được thực thi bên trong context này.

Execution Context có thể được hiểu như là một vùng chứa mà trong đó JavaScript engine theo dõi quá trình thực thi code, quản lý các variable và function.

Execution context gồm có 2 phần:

- **Thread of execution**: Đi qua từng dòng code và thực thi từng dòng.
- **Memory**: Lưu dữ liệu (variables) và code (function) để sử dụng.

### Hosting

Khi một execution context được khởi tạo, **hoisting** xảy ra. Hoisting là một cơ chế đặc biệt trong JavaScript, nơi mà các khai báo variable và function được "nâng/đẩy" lên đầu của scope hiện tại trước khi code thực sự được thực thi. Dễ hiểu thì nó là quá trình thiết lập memory space cho các variable và function.

#### Hoisting với `var`

Khi khai báo variable bằng `var`, biến được hoisted nhưng chỉ khởi tạo với giá trị undefined cho đến khi nó thực sự được gán giá trị trong quá trình thực thi.

```js
console.log(a); // undefined
var a = 5;
console.log(a); // 5
```

Trong ví dụ này, JavaScript engine hiểu code như sau:

```js
var a;
console.log(a); // undefined
a = 5;
console.log(a); // 5
```

Variable `a` được hoisted lên đầu, nhưng giá trị của nó chưa được gán ngay lập tức, dẫn đến kết quả `undefined` khi lần đầu tiên in ra `console.log(a);`.

#### Hoisting với `let` và `const`

Variable khai báo bằng `let` và `const` thì cũng được hoisted nhưng không được khởi tạo ngay lập tức. Thay vào đó, chúng nằm trong một temporal dead zone, và chỉ có thể được sử dụng sau khi đã được khai báo.

```js
console.log(b); // ReferenceError: Cannot access 'b' before initialization
let b = 10;
console.log(b); // 10
```

Với `let` và `const`, biến `b` được hoisted, nhưng việc truy cập nó trước khi khai báo sẽ dẫn đến lỗi `ReferenceError`. JavaScript engine vẫn biết về sự tồn tại của biến `b`, nhưng nó chỉ được khởi tạo khi thread of execution đi đến dòng code khai báo biến `b` và thực thi dòng code.

#### Hoisting với function

Hoisting cũng áp dụng cho các khai báo hàm (function declaration). Khi khai báo một hàm, toàn bộ định nghĩa của hàm được hoisted lên đầu phạm vi hiện tại, cho phép bạn gọi hàm trước khi nó xuất hiện trong mã.

```js
greet(); // "Hello!"
function greet() {
  console.log("Hello!");
}
```

Trong ví dụ này, func `greet` có thể được gọi trước khi định nghĩa của nó xuất hiện trong mã, bởi vì toàn bộ hàm đã được hoisted.

#### Hoisting với Function Expressions và Arrow Functions

Function expressions và arrow functions được xử lý như các variable, tức là chỉ có tên biến được hoisted, nhưng hàm không được khởi tạo cho đến khi thread of execution đi đến dòng code khai báo hàm.

```js
sayHello(); // TypeError: sayHello is not a function
var sayHello = function () {
  console.log("Hello!");
};
```

Trong trường hợp này, `sayHello` được hoisted giống như một variable khai báo bằng `var`, và giá trị ban đầu của nó là `undefined`. Khi cố gắng gọi nó trước khi được khởi tạo sẽ dẫn đến lỗi `TypeError`.

## Call Stack

JavaScript sử dụng một cơ chế gọi là **Call Stack** để quản lý các execution context - nó giúp theo dõi ta đang ở execution context nào - nghĩa là function nào đang được thực thi.

Khi chương trình bắt đầu, global execution context là context đầu tiên được đẩy vào call stack. Mỗi lần một hàm được gọi, một function execution context mới được tạo và đẩy lên đỉnh của call stack. Khi hàm hoàn thành, context của hàm đó sẽ được bật ra khỏi call stack, và JavaScript tiếp tục với context trước đó. Nó hoạt động theo cơ chế LIFO (last in first out).

Tạm thời lý thuyết là vậy, chúng ta sẽ hiểu vai trò của chúng sau khi xem qua ví dụ dưới đây.

## Ta có một chương trình nhỏ sau:

![](https://images.viblo.asia/df6c61fc-86ea-41ec-9316-b3098af07580.jpeg)

Khi chúng ta chạy chương trình trên trên, một **global execution context** sẽ được tạo ra kèm **global memory**, trong call stack lúc này thì chúng ta đang ở **global()**.

![](https://images.viblo.asia/2e265137-47f2-4c1d-a2a7-58d16a55752e.jpeg)

Lúc này, **thread of execution** sẽ thực thi vai trò của nó là đi qua từng dòng code và thực thi lần luợt, như sau:

- **Dòng 1**: Khai báo một constant `num` ở global memory và gán giá trị cho nó là 3
- **Dòng 3**: Khai báo function multiplyBy2 ở global memory
- **Dòng 8**: Khai báo một constant `output` và giá trị của nó lúc này là chưa xác định, lý do? Vì ta gán cho nó `multiplyBy2(num)` - lúc này chưa xác định được giá trị.

Toàn cảnh tạm thời của ta đang có:

![](https://images.viblo.asia/7b808a59-90ef-4e1a-9bad-c3aa3ace53d8.jpeg)

Ta giải quyết bằng cách gọi function `multiplyBy2` và truyền vào argument `num`. Giá trị của `num` là gì? Đi đến **global memory** để tìm và nhận được giá trị là `3`.
Sau đó tiến hành gọi function `multiplyBy2(3)`.

Như đã tìm hiểu ở phần lý thuyết, mỗi khi ta gọi một function thì một **function execution context** tương ứng sẽ được tạo ra để thực thi code của function đó.

Lúc này, `multiplyBy2(3)` cũng sẽ được đẩy vào call stack.

![](https://images.viblo.asia/52a8a7b7-77f1-47b8-9d78-fe5db07899c8.jpeg)

Lúc này ta đang ở function execution context của multiplyBy2(3), và thread of execution lại tiếp tục thực hiện nhiệm vụ của mình:

- Gán giá trị cho parameter `inputNumber`: 3
- Khai báo một constant `result` ở local memory và gán giá trị cho nó là: `3 * 2: 6`
- `return result;`
  - 1. JavaScript sẽ đi đến local memory và tìm giá trị của `result`: `6`.
  - 2. Lấy giá trị vừa tìm được và return (trả về) cho constant `output` ở global memory.

![](https://images.viblo.asia/785acdfa-0edb-4b58-bfb6-915d6f8a13f8.jpeg)

Vậy là đã hoàn thành, function execution context ở trên sẽ được cleared (xoá) - `multiplyBy2(3)` sẽ bị lấy ra khỏi call stack và ta trở lại **global().**

![](https://images.viblo.asia/63cd3d49-14d4-473d-9d9b-66bbcc6fb76c.jpeg)

Thread of execution lại tiếp tục làm nhiệm vụ của mình, đi đến và thực thi dòng code tiếp theo.

- **Dòng 9**: Khai báo một constant `newOutput` và gán giá trị cho nó là `multiplyBy2(10)`. Tương tự như khi thực thi **Dòng 8** nên chúng ta sẽ đi nhanh hơn.
  - `multiplyBy2(10)` được đẩy vào call stack
  - Một function execution context tương ứng được tạo ra để thực thi.
  - Thực thi từng dòng, và trả giá trị đã tính toán được cho `newOutput` ở global memory

![](https://images.viblo.asia/41b8717f-9a20-4cef-9d65-faf81b9e46e9.jpeg)

Do đã thực thi xong nên function execution context ở trên sẽ được xoá. Lúc này `multiplyBy2(10)` sẽ bị lấy ra khỏi stack và ta trở lại **global()**.

![](https://images.viblo.asia/82c98394-78b8-446d-9198-86a5c93c9251.jpeg)

Vì chương trình đã hoàn thành nên global execution context cũng sẽ được cleared luôn.
