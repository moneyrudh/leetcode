function isValidSudoku(board: string[][]): boolean {
    let t: string[][] = new Array(9).fill(new Array(9));
    let m1: Map<string, number> = new Map<string, number>();
    let m2: Map<string, number> = new Map<string, number>();
    let m3: Map<string, number> = new Map<string, number>();
    const n = board.length;
    let row=0, col=0;
    let _row='', _col='', _box='';
    for(let i=0; i<n; i++) {
        m1.clear();
        m2.clear();
        m3.clear();
        for(let j=0; j<n; j++) {
            row = Math.trunc(i/3)*3 + Math.trunc(j/3);
            col = (i%3)*3 + j%3;
            
            _row=board[i][j];
            _col=board[j][i];
            _box=board[row][col];

            if(_row != '.' && m1.has(_row)) return false;
            if(_col != '.' && m2.has(_col)) return false;
            if(_box != '.' && m3.has(_box)) return false;

            m1.set(_row, 1);
            m2.set(_col, 1);
            m3.set(_box, 1);
        }
    }
    return true;
};
