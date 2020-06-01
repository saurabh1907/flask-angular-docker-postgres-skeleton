export class Blog {
    public title?: string;
    public description?: string;
    public id?: number;
    public created_date?: Date;

    // convert json values into object
    constructor(values: Object = {}) {
        Object.assign(this, values);
    }
}
