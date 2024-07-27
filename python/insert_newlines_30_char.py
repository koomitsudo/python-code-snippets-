def newline30(strings):
    # 文字列の全体の長さ
    strings_len = len(strings)
    # 区切り文字のリスト
    separate_chars = ['、', '。', '　']
    # 1行の文字数
    line_count = 0
    # 次の行の先頭位置を記憶
    start_offset = 0
    # 結果リスト
    result = []
    # チェック中の文字インデックス
    offset = 0

    while offset < strings_len:
        # 句読点または空白で、かつ30文字以上の場合改行
        if strings[offset] in separate_chars and line_count >= 30:
            result.append(strings[start_offset:offset + 1])
            start_offset = offset + 1
            line_count = 0
        else:
            line_count += 1
        offset += 1

    # 残りの文字を追加
    result.append(strings[start_offset:])
    return "\n".join(result)

if __name__ == "__main__":
    value = newline30('１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３、４５６７８９０、１２３４５６７８９０。')
    print(value)