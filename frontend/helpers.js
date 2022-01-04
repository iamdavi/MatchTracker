/**
 * Función que genera objetos con propiedades que pueden modificar el estado
 * del vuex generando los getters uy los setters de los campos pasados en las
 * opciones.
 * 
 * @param { options } options Objeto que contiene la información de las propiedades
 * 														de las que hay que optener los getters y los setters.
 * 														Debe contener las propiedades 'fields', 'base', 'mutations'
 * 														de la siguiente manera:
 * 															options: {
 * 																fields: ["nombre", "descripcion", "color"],
 * 																base: "equipo",
 * 																mutation: "updateEquipo"
 * 															}
 * @returns 	Devuelve un objeto con las propiedades pasadas y con los getters 
 * 						y setters generados
 */
export function mapFields(options) {
  const object = {};
  for (let x = 0; x < options.fields.length; x++) {
    const field = [options.fields[x]];
    object[field] = {
      get() {
        return this.$store.state[options.base][options.base][field];
      },
      set(value) {
        this.$store.commit(options.mutation, { [field]: value });
      }
    };
  }
  return object;
}