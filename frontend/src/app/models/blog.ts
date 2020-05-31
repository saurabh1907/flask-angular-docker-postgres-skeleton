export class Blog {
    public title?: string;
    public description?: string;
    public id?: number;
    public createdAt?: Date;

    // convert json values into object
    constructor(values: Object = {}) {
        Object.assign(this, values);
    }
}
